import os
import requests
import schedule
import time
from instagrapi import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Instagram Credentials
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

cl = Client()
cl.login(USERNAME, PASSWORD)

# Function to generate content using Gemini API
def generate_content():
    prompt = "Generate an engaging Instagram post about AI and technology."
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return text.split("\n\n")[0]  # Extract the first option
        except (KeyError, IndexError):
            return "Error extracting content"
    else:
        return "Error with API request"
    
# Function to post on Instagram
def post_on_instagram(image_path, caption):
    try:
        cl.photo_upload(image_path, caption)
        print("Post uploaded successfully!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Run the scheduler until post is published
image_path = "image.png"
caption = generate_content()
post_time = "15:19"  # Default posting time

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == post_time:
        if post_on_instagram(image_path, caption):
            print("The scheduled post has been successfully published!")
            break
    time.sleep(30)
