from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

image_path = "image.jpg"
caption = "Hello, Instagram! #Python"

cl.photo_upload(image_path, caption)
print("Post uploaded successfully!")
