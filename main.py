import collections
def create_user_dict():
        return collections.UserDict()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()