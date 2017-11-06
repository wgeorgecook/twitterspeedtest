#! /usr/bin/python3

# Will run library to check the speed, returns result

import fastdotcom


class FastChecker(object):
    """
    Checks speed from fast.com and returns in mbps.
    """

    def __init__(self):
        self.speed = fastdotcom.fast_com()


    def check_speed(self):

        print("### Checking Speed Now ###")
        print("### Speed is {} ###".format(self.speed))
        return self.speed