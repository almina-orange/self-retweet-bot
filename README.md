# self-retweet-bot

## Info

* 自動RT用レポジトリ
* 自ツイート＋ハッシュタグで判定
* 定期的にランダムでRTする


## Files

```
.
├── venv
├── __pycache__
├── .gitignore
├── Procfile                # Heroku process setting
├── requirements.txt        # python package list
├── .env                    # key information for access
├── README.md               # this
├── scheduler.py            # scheduling
├── LINE_notify.py          # post message to LINE Notify
├── twitter_func.py         # Twitter API functions
├── get_all_tweets.py       # get all tweets from self timeline
├── get_works.py            # get only target tweets (e.g. works...)
├── post_self_retweet.py    # post self-retweet to target tweet
├── post_all_unretweet.py   # reset all self-retweet
├── script_on_local.py      # script on local
├── out.json                # all tweets
└── work.json               # all target tweets
```


## Usage

* アクセス情報を `.env` として作成する

    ```sh
    # Twitter api key
    CONSUMER_KEY="N7jWmgCNfpxppcY5ZFa4Urou9"
    CONSUMER_SECRET="3lxaJ043KFPMJlLSV0M32fbzuoKTJmwHlcizfkDHFLJI68LxYX"
    ACCESS_TOKEN="3149630647-rOnv0SSTYp8c61n3KpmKfDjoUlqaxcmlswQznc1"
    ACCESS_TOKEN_SECRET="8bcAQM55PGEbWxqlfFo8AwMQzOtAnEsakCKVhxAy702Za"
    SCREEN_NAME="Code4_11"

    # LINE Notify api key
    LINE_NOTIFY_ACCESS_TOKEN="JPM2AWZ6sGgVRUbOYk00wtbmSq3ld7yKUijxHJFSOpe"
    ```

* ローカル環境で実行する際には `dotenv` で `.env` を読み込むˇ

    ```python
    from dotenv import load_dotenv
    import os

    def main():

        # Load env-vars from `.env`
        load_dotenv()

        # Main job
        # os.system('python get_all_tweets.py')

    if __name__ == "__main__":
        main()
    ```

* 定期実行を `scheduler.py` で設定

    ```python
    from apscheduler.schedulers.blocking import BlockingScheduler
    import os

    from LINE_notify import post_line_notify

    def job():

        # Post to LINE-Notify
        os.system('python get_all_tweets.py')
        post_line_notify('Job done.')


    def main():

        sched = BlockingScheduler()

        # Job setting
        # sched.add_job(job, 'cron', hour=8)
        # sched.add_job(job, 'cron', day_of_week='sun')

        sched.start()


    if __name__ == "__main__":
        main()
    ```

* Heroku 上で稼働させるプロセスを `Procfile` で設定

    ```
    bot: python scheduler.py
    ```

* プロセスに dyno を割り当てて稼働させる

    ```sh
    $ heroku ps:scale bot=1
    ```

* プロセスを停止するときは dyno の割り当てを 0 にする

    ```sh
    $ heroku ps:scale bot=0
    ```


Note
* 各エンドポイントにはリクエスト回数に制限がある
* リクエスト回数の確認もプログラムで可能（`requests.py`を参照）
* 基本的にはプログラム変更時もプロセスを止めなくて良い


## Ref

* [Docs — Twitter Developers](https://developer.twitter.com/en/docs.html)
* [PythonでTwitter API を利用していろいろ遊んでみる - Qiita](https://qiita.com/bakira/items/00743d10ec42993f85eb)
* [140文字以上のツイートを取得する - Qiita](https://qiita.com/hitsumabushi845/items/f7fd87106381fc65fc86)
* [herokuでのスケジュール管理にAPSchedulerを使ってみる - ストックドッグ](http://www.stockdog.work/entry/2017/04/10/003452)
* [herokuでアドオン使わずにcron (Python) - 木魚ブログ](http://sainoky.hatenablog.com/entry/2015/05/24/200949)
* [pythonのAPSchedulerによるプログラム、関数の定期実行 - どん底から這い上がるまでの記録](https://www.pytry3g.com/entry/apscheduler)
* [PythonからLINE NotifyでLINEにメッセージを送る - Qiita](https://qiita.com/tadaken3/items/0998c18df11d4a1c7427)