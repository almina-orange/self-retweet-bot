import json, config
from requests_oauthlib import OAuth1Session
import datetime, time

""" Connect session """
# auth key
CX = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# connect
twitter = OAuth1Session(CX, CS, AT, ATS)

""" Get timeline from my account """
# endpoint for request timeline
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# access to endpoint
res = twitter.get(url)

# output status
limit = res.headers['x-rate-limit-remaining']  # remained requests
reset = res.headers['x-rate-limit-reset']  # UTC time to reset remeained requests
sec = int(res.headers['X-Rate-Limit-Reset']) \
     - time.mktime(datetime.datetime.now().timetuple())  # second to reset

print("limit: " + limit)
print("reset: " + reset)
print("reset sec: %s" % sec)