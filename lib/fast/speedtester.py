#! /usr/bin/python3

# Will run library to check the speed, returns result

import fastdotcom
from datetime import datetime


class Fast_checker(object):
    """
    Checks speed from fast.com and returns in mbps.
    """

    def check_speed(self):
        speed = fastdotcom.fast_com()
        return speed



