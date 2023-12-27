import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())