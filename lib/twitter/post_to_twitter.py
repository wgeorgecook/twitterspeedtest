
# All the tweepy stuff

import tweepy

from lib.fast.speedtester import fast_checker
from settings import CONSUMER_SETTINGS, ACCESS_SETTINGS



class Update_twitter(object):

    """
    Will gather speed from Fast_checker object, concatenate a new tweet with the speed, and update Twitter
    """

    # Twitter API information
    self.auth = auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
    self.auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))
    self.api = tweepy.API(auth)

    def new_tweet():
        timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
        return "At {0} download speed (rounded): {1} mbps".format(timestamp, int(Fast_checker.check_speed()))

    def update_status():
        tweet = self.new_tweet()
        api.update_status(tweet)

