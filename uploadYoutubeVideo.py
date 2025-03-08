import os
import time
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set the OAuth 2.0 scopes needed
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Get authenticated service
def get_authenticated_service():
    creds = None

    # Token file (to store refresh token for future use)
    token_file = 'token.json'
    
    # Load existing credentials (if available)
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file)

    # If there are no (valid) credentials, let user authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES
            )
            creds = flow.run_local_server(port=8080)  # This uses http://localhost:8080/

        # Save credentials for future use
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)

# Upload video function
def upload_video(youtube, file_path, title, description, tags, category_id="22", privacy_status="public"):
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": privacy_status,
        },
    }

    # Set video file to upload
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True, mimetype="video/*")

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploading... {int(status.progress() * 100)}% complete")
        time.sleep(1)

    print("Upload Complete!")
    print(f"Video ID: {response['id']}")

# Main function
if __name__ == "__main__":
    youtube_service = get_authenticated_service()

    # Video Metadata
    video_file = "video.mp4"   # Replace with your video file path
    video_title = "My Python Upload Video"
    video_description = "This video was uploaded via Python script using YouTube Data API v3."
    video_tags = ["python", "youtube api", "automation"]
    video_category = "22"  # Category 22 is 'People & Blogs'

    upload_video(
        youtube_service,
        file_path=video_file,
        title=video_title,
        description=video_description,
        tags=video_tags,
        category_id=video_category,
        privacy_status="public"
    )
