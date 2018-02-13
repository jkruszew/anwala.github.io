# Import the necessary methods from different libraries
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
from sys import stdout

# Variables that contains the user credentials to access Twitter API
#access_token = "enter token here"
#access_token_secret = "enter token here"
#consumer_key = "enter key here"
#consumer_secret = "enter key here"

consumer_key = '5j7SmACEOyPsKN12MPXrPQbw4'
consumer_secret = 'WrDMatcCi3P8lLHVgMQYW5LLMOLbc6gNd3wJxU4pPcrCnINYFG'
access_token = '958478661920940032-ddyuERsryUYMYfIEdn50StAdDVegltk'
access_token_secret = 'rheoQZNorAzfGqfuDmRh4iiuS3fmy99oslPfQcq4bnqHn'

# Accessing tweepy API
# api = tweepy.API(auth)

# This is a basic listener that just prints received tweets to stdout.
count = 100000000 # moved outside of class definition to avoid getting reset

class StdOutListener(StreamListener):
    def on_data(self, data):

        decoded = json.loads(data)

        global count # get the count
        if count <= 0:
            import sys
            sys.exit()
        else:
            try:
                for url in decoded["entities"]["urls"]:
                    print(count, ':', "%s" % url["expanded_url"] + "\r\n")
                    print("%s" % url["expanded_url"], file=open("InitialURLList.txt", "a"))
                    count -= 1

            except KeyError:
                print(decoded.keys())

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['Olympics', 'Football', 'WorldCup', 'Soccer', 'Sports'])


