import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()