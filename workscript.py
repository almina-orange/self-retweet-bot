import json, config
from requests_oauthlib import OAuth1Session

""" Connect session """
# auth key
CX = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# connect
twitter = OAuth1Session(CX, CS, AT, ATS)

""" Setting endpoint """
# endpoint for request timeline
# ref: https://developer.twitter.com/en/docs/

# GET endpoint
# url = "https://api.twitter.com/1.1/followers/ids.json"  # get follower info only id
# url = "https://api.twitter.com/1.1/followers/list.json"  # get follower info
# url = "https://api.twitter.com/1.1/friends/list.json"  # get follow info
# url = "https://api.twitter.com/1.1/lists/list.json"  # get follow info

# url = "https://api.twitter.com/1.1/account/settings.json"  # get self-account settings
# url = "https://api.twitter.com/1.1/account/verify_credentials.json"  # get self-account info
# url = "https://api.twitter.com/1.1/users/profile_banner.json?screen_name=Code4_11"  # get self-account banner info

url = "https://api.twitter.com/1.1/statuses/show.json?id=1147920210818560000"  # get tweet info
# url = "https://api.twitter.com/1.1/statuses/lookup.json?id=1153514750048755712"  # get tweet info detail
# url = "https://api.twitter.com/1.1/statuses/retweets/1151895176098406401.json"  # get retweet status
# url = "https://api.twitter.com/1.1/statuses/retweets_of_me.json"  # get retweeted tweets
# url = "https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=1151895176098406401&stringify_ids=true"  # get retweeters info only id
# url = "https://api.twitter.com/1.1/favorites/list.json?screen_name=Code4_11"  # get retweeters info only id

# url = "https://api.twitter.com/1.1/statuses/user_timeline.json"  # get self timeline
# url = "https://api.twitter.com/1.1/statuses/home_timeline.json"  # get home timeline
# url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"  # get home timeline

# url = "https://api.twitter.com/1.1/search/tweets.json?q=Code4_11"  # search tweets


""" Access to API """
# access to endpoint
params = {
    'count': 100,
    'tweet_mode': 'extended',
}
res = twitter.get(url, params = params)

if res.status_code == 200:
    # output
    timelines = json.loads(res.text)
    # for line in timelines:
    #     print('id: ' + line['id_str'])
    #     print('text: ' + line['text'])
    #     # print('favorite_count: ' + str(line['favorite_count']))
    #     # print('retweet_count: ' + str(line['retweet_count']))
    #     # print('retweeted: ' + str(line['retweeted']))
    #     print("------")
    print(json.dumps(timelines, sort_keys = True, indent = 4))
    with open('tmp.json', 'w') as f:
        json.dump(timelines, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
else:
    print("Failed: %d" % res.status_code)