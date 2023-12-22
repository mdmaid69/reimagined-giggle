import datetime
def get_current_date():
        return datetime.date.today()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()