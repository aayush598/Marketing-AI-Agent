import os
import requests
import time
import streamlit as st
from instagrapi import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

cl = Client()
cl.login(USERNAME, PASSWORD)

# Function to generate content using Gemini API
def generate_content(prompt):
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
        st.success("Post uploaded successfully!")
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Streamlit UI
st.title("Instagram AI Content Scheduler")
prompt = st.text_input("Enter prompt for AI-generated caption:", "Generate an engaging Instagram post about AI and technology.")
image_path = st.text_input("Enter image path:", "default_image.jpg")
post_time = st.text_input("Enter scheduled post time (HH:MM, 24-hour format):", "14:39")

if st.button("Generate & Schedule Post"):
    caption = generate_content(prompt)
    st.write("Generated Caption:", caption)
    
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == post_time:
            if post_on_instagram(image_path, caption):
                st.write("The scheduled post has been successfully published!")
                break
        time.sleep(30)
