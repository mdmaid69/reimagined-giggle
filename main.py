import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import time
def get_time_since_epoch():
        return time.time()