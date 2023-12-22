import math
def calculate_arc_sine(x):
        return math.asin(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()