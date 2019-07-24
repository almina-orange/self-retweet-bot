""" Functions for twitter API """

import random
import json, config
from requests_oauthlib import OAuth1Session


def connect_sess():

    """ Connect session """

    # auth key
    CX = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    # connection
    return OAuth1Session(CX, CS, AT, ATS)


def get_user_timeline(twitter, params, debug: bool = False):
    
    """ Get timeline from my account """

    # endpoint for post tweet
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"  # get self timeline

    # access to endpoint
    res = twitter.get(url, params = params)

    if res.status_code == 200:
        # output
        if debug:
            print("Succeeded.")
        return json.loads(res.text)
    else:
        print("Failed. : %d" % res.status_code)


def get_tweet_info(twitter, params, debug: bool = False):
    
    """ Get tweet information """

    # endpoint for post tweet
    url = "https://api.twitter.com/1.1/statuses/show.json"  # get tweet info

    # access to endpoint
    res = twitter.get(url, params = params)

    if res.status_code == 200:
        # output
        if debug:
            print("Succeeded.")
        return json.loads(res.text)
    else:
        print("Failed. : %d" % res.status_code)


def post_retweet(twitter, params, debug: bool = False):
    
    """ Post retweet """

    # endpoint for post tweet
    url = "https://api.twitter.com/1.1/statuses/retweet.json"  # post retweet

    # access to endpoint
    res = twitter.post(url, params = params)

    if res.status_code == 200:
        # output
        if debug:
            print("Succeeded.")
        return json.loads(res.text)
    else:
        print("Failed. : %d" % res.status_code)


def post_unretweet(twitter, params, debug: bool = False):
    
    """ Post unretweet """

    # endpoint for post tweet
    url = "https://api.twitter.com/1.1/statuses/unretweet.json"  # post unretweet

    # access to endpoint
    res = twitter.post(url, params = params)

    if res.status_code == 200:
        # output
        if debug:
            print("Succeeded.")
        return json.loads(res.text)
    else:
        print("Failed. : %d" % res.status_code)