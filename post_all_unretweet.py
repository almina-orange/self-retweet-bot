import random
import json, config
from requests_oauthlib import OAuth1Session

from twitter_func import connect_sess
from twitter_func import post_unretweet


def main():

    """ Load tweet ids """
    with open('work.json', 'r') as f:
        data = json.load(f)

    ids = data['id']


    """ Connect session """
    # auth key
    CX = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    # connect
    twitter = connect_sess()
    for tar_id in ids:
        post_unretweet(twitter, {'id': tar_id})

    print("Succeeded.")


if __name__ == "__main__":
    main()