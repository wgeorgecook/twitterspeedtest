#! /usr/bin/python3

# Will run library to check the speed, returns result

import fastdotcom
from datetime import datetime


def check_speed():
    speed = fastdotcom.fast_com()
    return speed


def new_tweet():
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
    return "At {0} download speed (rounded): {1} mbps".format(timestamp, int(check_speed()))
