import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()