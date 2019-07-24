import random
import json, config
from requests_oauthlib import OAuth1Session

from twitter_func import connect_sess
from twitter_func import get_tweet_info
from twitter_func import post_retweet
from twitter_func import post_unretweet


def main():

    ### Choice tweet randomly
    with open('work.json', 'r') as f:
        data = json.load(f)

    tar_id = random.choice(data['id'])


    ### Check target tweet
    twitter = connect_sess()
    params = {
        'id': tar_id,
        'tweet_mode': 'extended',
    }
    tweet = get_tweet_info(twitter, params)

    print('id: ' + tweet['id_str'])
    print('text: ' + tweet['full_text'])
    print("------")
    # print(json.dumps(tweet, sort_keys = True, indent = 4))


    ### Unretweet (if already self-retweeted)
    if tweet['retweeted']:
        post_unretweet(twitter, {'id': tar_id})


    ### Self-retweet
    post_retweet(twitter, {'id': tar_id})


if __name__ == "__main__":
    main()