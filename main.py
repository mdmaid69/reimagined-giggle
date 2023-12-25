import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)