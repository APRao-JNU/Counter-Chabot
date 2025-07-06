# Twitter/X stream example
import tweepy, requests, os
from dotenv import load_dotenv
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        response = requests.post("http://localhost:8000/counter-reply",
                                 json={"text": tweet.text})
        reply = response.json()["reply"]
        client.create_tweet(text=reply, in_reply_to_tweet_id=tweet.id)

stream = MyStream(bearer_token=BEARER_TOKEN)
stream.add_rules(tweepy.StreamRule("capitalism OR socialism OR ideology"))
stream.filter()
