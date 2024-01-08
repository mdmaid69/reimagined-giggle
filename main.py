import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()