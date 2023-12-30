import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))