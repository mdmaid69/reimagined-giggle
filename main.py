import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()