#coding:UTF-8
import schedule
import time

import get_all_tweets
import get_works
import post_self_retweet

from LINE_notify import post_line_notify


def job_everyweek():

    get_all_tweets.main()
    get_works.main()

    ### Post to LINE-Notify
    post_line_notify('everyweek')


def job_everyday():

    post_self_retweet.main()

    ### Post to LINE-Notify
    post_line_notify('everyday')


def job_everyhour():

    ### Post to LINE-Notify
    post_line_notify('everyhour')


def job_everyminute():

    ### Post to LINE-Notify
    post_line_notify('everyminute')


def main():
    schedule.every().sunday.do(job_everyweek)
    schedule.every().day.at("7:00").do(job_everyday)
    schedule.every().hour.do(job_everyhour)

    # schedule.every(1).minutes.do(job_everyweek)
    # schedule.every(1).minutes.do(job_everyday)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()