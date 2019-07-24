import json, os
from requests_oauthlib import OAuth1Session

from twitter_func import connect_sess
from twitter_func import get_user_timeline


def main():

    SN = os.environ.get('SECRET_NAME','')

    ### First access
    twitter = connect_sess()
    params = {
        'count': 100,
        'screen_name': SN,
        'tweet_mode': 'extended',  # to get full-text
    }
    timelines = get_user_timeline(twitter, params)


    ### Get all tweet from self timeline
    all_tweets = []
    while len(timelines) > 0:
        all_tweets = all_tweets + timelines

        # more get...
        params['max_id'] = timelines[len(timelines) - 1]['id'] - 1
        timelines = get_user_timeline(twitter, params)

    print("------------------------------------")
    print('all_tweets: ' + str(len(all_tweets)))


    ### Save
    with open('out.json', 'w') as f:
        json.dump(all_tweets, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


if __name__ == "__main__":
    main()