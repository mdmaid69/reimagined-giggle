import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)