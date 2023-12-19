import itertools
print(list(itertools.permutations([1, 2, 3])))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()