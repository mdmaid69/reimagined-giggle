import time
def get_current_time():
        return time.ctime()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread