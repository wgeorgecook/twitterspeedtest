# Runs the Python job

from lib.twitter.post_to_twitter import UpdateTwitter

push = UpdateTwitter()

push.update_status()
