#coding:UTF-8
from apscheduler.schedulers.blocking import BlockingScheduler
import os

from LINE_notify import post_line_notify


def week_job():

    os.system('python get_all_tweets.py')
    os.system('python get_works.py')

    ### Post to LINE-Notify
    post_line_notify('everyweek')


def day_job():

    os.system('python post_self_retweet.py')

    ### Post to LINE-Notify
    post_line_notify('everyday')


def main():

    ### Initial process

    os.system('python get_all_tweets.py')
    os.system('python works.py')


    ### Set scheduler

    sched = BlockingScheduler()

    sched.add_job(day_job, 'cron', hour=8)
    sched.add_job(week_job, 'cron', day_of_week='sun')

    sched.start()


if __name__ == "__main__":
    main()