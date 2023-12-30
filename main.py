import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import datetime
def get_current_date():
        return datetime.date.today()