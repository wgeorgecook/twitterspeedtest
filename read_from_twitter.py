#! /usr/bin/python3

# All the tweepy stuff

import tweepy
from settings import CONSUMER_SETTINGS, ACCESS_SETTINGS


auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))

api = tweepy.API(auth)



def read_status(username):
    user_tweets = api.user_timeline(id=username, count=1)
    for status in user_tweets:
        return status.author, status.user
