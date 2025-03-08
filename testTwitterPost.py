from twitterPost import TwitterClient
import os
from dotenv import load_dotenv

load_dotenv()

# Example usage:
if __name__ == "__main__":
    # Replace with your credentials
    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    twitter_client = TwitterClient(
        BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )
    response = twitter_client.post_tweet("Hello, X! This is an automated tweet using a modular Twitter client.")
    print(response)