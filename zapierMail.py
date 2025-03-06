import requests
import os
from dotenv import load_dotenv

load_dotenv()

ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")

data = {
    "subject": "Automated Email Notification",
    "body": "Your system has successfully run!",
    "recipient": "recipient@example.com"
}

requests.post(ZAPIER_WEBHOOK_URL, json=data)
