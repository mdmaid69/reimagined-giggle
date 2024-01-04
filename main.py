import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()