import datetime
def get_current_datetime():
        return datetime.datetime.now()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()