#coding:UTF-8
import schedule
import time


def job1():
    #ここにメインの処理を書く
    print("Time has come! (1 min...)")


def job2():
    #ここにメインの処理を書く
    print("Time has come! (2 min...)")


def main():
    #10分毎にjobを実行
    schedule.every(1).minutes.do(job1)
    schedule.every(2).minutes.do(job2)

    # #毎時間ごとにjobを実行
    # schedule.every().hour.do(job)

    # #AM10:30にjobを実行
    # schedule.every().day.at("10:30").do(job)

    # #月曜日にjobを実行
    # schedule.every().monday.do(job)

    # #水曜日の13:15にjobを実行
    # schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()