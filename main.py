import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread