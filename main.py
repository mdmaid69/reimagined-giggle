import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()