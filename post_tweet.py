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

""" Get timeline from my account """
# endpoint for post tweet
url = "https://api.twitter.com/1.1/statuses/update.json"

# input tweet
print("Please input tweet:")
tweet = input('>> ')
print("*******************************************")

# access to endpoint
params = {"status": tweet}
res = twitter.post(url, params = params)

if res.status_code == 200:
    print("Succeeded.")
else:
    print("Failed. : %d" % res.status_code)