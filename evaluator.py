from gather_data import *


consumer_key = "XXXXX"
consumer_secret = "XXXXX"
access_token = "XXXXX"
access_token_secret = "XXXXX"


# access_token = "873881805119672322-kwWJeoffxEAiWNbwMnqOpP9uODLCr6T"
# access_token_secret = "mw7O66clhLADSgWfJeud22rBSYLN5tfcSfXrpivJcfkCq"
# consumer_key = "as1VRfqFjInsrx6uSuweettWy"
# consumer_secret = "UK60ZYwV89zoP9ajknnhGrN7eYhOWPzGS2NeGXUP9SJNPt7r46"


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