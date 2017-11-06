
# All the tweepy stuff

import tweepy
from datetime import datetime
from lib.fast.speedtester import FastChecker
from settings import CONSUMER_SETTINGS, ACCESS_SETTINGS



class UpdateTwitter(object):

    """
    Will gather speed from Fast_checker object, concatenate a new tweet with the speed, and update Twitter
    """
    def __init__(self):
        # Twitter API information
        self.auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
        self.auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))
        self.api = tweepy.API(self.auth)

        self.fast = FastChecker()

    def new_tweet(self):
        timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
        return "At {0} download speed: {1} mbps".format(timestamp, float(self.fast.check_speed()))

    def update_status(self):
        tweet = self.new_tweet()
        print("### Posting tweet: {} ###".format(tweet))
        self.api.update_status(tweet)
        print("### Tweet posted! ###")

