import tweepy
import json
with open("data.json") as f: data = json.load(f)

auth = tweepy.OAuthHandler(data["consumer_key"], data["consumer_secret"])
auth.set_access_token(data["access_key"], data["access_secret"])

REST = tweepy.API(auth)


class CustomListener(tweepy.StreamListener):
    def __init__(self, fnc):
        super().__init__()
        self.fnc = fnc

    def on_status(self, status):
        return self.fnc(status)

    def on_error(self, status):
        print(status)


STREAM = lambda fnc: tweepy.Stream(auth, CustomListener(fnc))
