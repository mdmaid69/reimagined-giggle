import math
def calculate_ceiling(x):
        return math.ceil(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()