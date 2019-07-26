#coding:UTF-8

""" Post to LINE-Notify
ref: https://qiita.com/tadaken3/items/0998c18df11d4a1c7427
"""

import os
import requests

def post_line_notify(msg):

    LAT = os.environ.get('LINE_NOTIFY_ACCESS_TOKEN','')

    url = "https://notify-api.line.me/api/notify"
    token = LAT

    headers = {"Authorization": "Bearer "+ token}
    payload = {"message":  msg}

    r = requests.post(url ,headers=headers ,params=payload)
