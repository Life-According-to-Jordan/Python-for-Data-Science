'''
BEFORE YOU START
Register for Twitter API: https://apps.twitter.com/
Install Dependencies:
    [pip install tweepy]
    [pip install textblob]
'''

#Used to access twitter API
import tweepy

#Used to perform sentiment analysis
from textblob import TextBlob

#Twitter Authentication 
consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
access_token = 'YOUR ACCESS TOKEN'
access_token_secret = 'YOUR ACCESS TOKEN SECRET'

#OAuth authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#main variable from which we will work, single authentication arguement 
api = tweepy.API(auth)

#search for tweets
public_tweets = api.search('SEARCH KEY WORD HERE')

#method retrieves tweets to terminal 
#for loop in a list
for tweet in public_tweets:
    #string version of tweet
    print(tweet.text)
    #analysis of each tweet for the loop
    #polarity measures how positive or negative it is
    #subjectivity measures the degree of opinion or fact
    analysis = TextBlob(tweet.text)
    #this returns the sentiment of the tweet
    print(analysis.sentiment)
    print("")

'''
HELPFUL DEFINITIONS FOR SENTIMENT ANALYSIS
Natural Language Processing (NLP) - Branch of CS and AI that helps computers interpret human language.
Sentiment Analysis - computational analysis of text to determine the writter's attitude 
Tokenization - divides text into individual words 
Bag of Words (BOW) - method of extracting features from text
API - Application Programming Interface 
'''
