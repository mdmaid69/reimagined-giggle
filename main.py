import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()