#coding:UTF-8
from apscheduler.schedulers.blocking import BlockingScheduler
import time

import get_all_tweets
import get_works
import post_self_retweet

from LINE_notify import post_line_notify


def week_job():

    get_all_tweets.main()
    get_works.main()

    ### Post to LINE-Notify
    post_line_notify('everyweek')


def day_job():

    post_self_retweet.main()

    ### Post to LINE-Notify
    post_line_notify('everyday')


def hours_job():

    ### Post to LINE-Notify
    post_line_notify('everyhour')


def minutes_job():

    ### Post to LINE-Notify
    post_line_notify('every 30 minutes')


def main():

    sched = BlockingScheduler()

    # sched.add_job(minutes_job, 'interval', minutes=10)
    sched.add_job(hours_job, 'interval', hours=1)
    sched.add_job(day_job, 'cron', hour=8)
    sched.add_job(week_job, 'cron', day_of_week='sun')

    sched.start()


if __name__ == "__main__":
    main()