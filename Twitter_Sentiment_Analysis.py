#	1. Register for Twitter API
#	2. Install Dependencies
#   Write our Script

#Used to access twitter API
import tweepy
#Used to perform sentiment analysis
from textblob import TextBlob

consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'

access_token = 'YOUR ACCESS TOKEN'
access_token_secret = 'YOUR ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#search for tweets

public_tweets = api.search('Kitten')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    #this returns the sentiment of the tweet
    #polarity measures how positive or negative it is
    #subjectivity measures the degree of opinion or fact
    print(analysis.sentiment)
    print("")
