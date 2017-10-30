#! /usr/bin/python3

# All the tweepy stuff

import tweepy
from settings import CONSUMER_SETTINGS, ACCESS_SETTINGS
from speedtester import new_tweet


auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))

api = tweepy.API(auth)


def update_status():
    tweet = new_tweet()
    api.update_status(tweet)
