from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

# Login to Instagram
cl = Client()
cl.login(USERNAME, PASSWORD)

# Define recipient username and message
recipient_username = "target_user"  # Replace with the Instagram username
message = "I am busy right now, I will get back to you soon. This is an automated generated message."

# Get user ID
user_id = cl.user_id_from_username(recipient_username)

# Send message
cl.direct_send(message, [user_id])

print("Message sent successfully!")
