from apscheduler.schedulers.background import BackgroundScheduler
from .fetcher import add_to_db

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(add_to_db, 'interval', minutes=10)
    scheduler.start()