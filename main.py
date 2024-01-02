import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()