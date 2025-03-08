import tweepy

class TwitterClient:
    def __init__(self, bearer_token, consumer_key, consumer_secret, access_token, access_token_secret):
        """Initialize the Twitter API client."""
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

        self.client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True,
        )

    def post_tweet(self, text):
        """Posts a tweet with the given text."""
        try:
            response = self.client.create_tweet(text=text)
            print("Tweet posted successfully!")
            return response
        except tweepy.TweepyException as e:
            print(f"Error posting tweet: {e}")
            return None


