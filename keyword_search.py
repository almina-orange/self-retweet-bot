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

""" Search keyword in timeline """
# endpoint for request keyword search
url = "https://api.twitter.com/1.1/search/tweets.json"

# input keyword
print("Please input keyword.")
keyword = input('>> ')
print("************************************************")

# access to endpoint
params = {'q': keyword, 'count': 5}
res = twitter.get(url, params = params)

if res.status_code == 200:
    # output
    search_timeline = json.loads(res.text)
    for line in search_timeline['statuses']:
        print(line['user']['name'] + '::' + line['text'])
        print(line['created_at'])
        print("************************************************")
else:
    print("Failed: %d" % res.status_code)
