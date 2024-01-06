import collections
def create_ordered_dict():
        return collections.OrderedDict()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()