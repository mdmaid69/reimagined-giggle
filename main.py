import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)