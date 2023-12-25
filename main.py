import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import datetime
print(datetime.datetime.now())