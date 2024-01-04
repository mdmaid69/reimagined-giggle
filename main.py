import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)