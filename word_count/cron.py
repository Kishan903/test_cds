import logging

watcher_log = logging.getLogger("watcher_log")

def my_scheduled_job():
    watcher_log.error("Cronjob")
