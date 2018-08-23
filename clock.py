from apscheduler.schedulers.blocking import BlockingScheduler
import main

twische = BlockingScheduler()


@twische.scheduled_job('interval', minutes=1)
def timed_job():
    main.auto_tenki()


if __name__ == "__main__":
    main.auto_tenki()
    twische.start()



