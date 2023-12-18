import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))