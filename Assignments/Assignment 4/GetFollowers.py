# Import the necessary methods from different libraries
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
from sys import stdout
import time

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


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

userName = 'acnwala'

api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.get_user(userName)

followers = [["" for x in range(2)] for y in range(len(user.friends()))]

followers[0][0] = userName
followers[1][0] = len(user.friends())

count = 1;
for x in user.friends():
    followers[0][count] = x.screen_name
    followers[1][count] = len(x.friends())


for x in range(len(followers)):
    print(x, ": ", followers[0][x]," ", followers[1][x])