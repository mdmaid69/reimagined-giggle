import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))