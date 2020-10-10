from gather_data import *


consumer_key = "XXXXX"
consumer_secret = "XXXXX"
access_token = "XXXXX"
access_token_secret = "XXXXX"


def start_tweets_api():
    listener = TweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    print stream
    while True:
        try:
            stream.sample(languages=['en'])

        except Exception as ex:
            print str(ex)


if __name__ == "__main__":
    start_tweets_api()
