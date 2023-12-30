import datetime
def get_today_date():
        return datetime.date.today()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread