#coding:UTF-8
import schedule
import time

import get_all_tweets
import get_works
import post_self_retweet


def job_everyweek():

    get_all_tweets.main()
    get_works.main()


def job_everyday():

    post_self_retweet.main()


def main():
    schedule.every().sunday.do(job_everyweek)
    schedule.every().day.at("16:00").do(job_everyday)

    # schedule.every(1).minutes.do(job_everyweek)
    # schedule.every(1).minutes.do(job_everyday)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()