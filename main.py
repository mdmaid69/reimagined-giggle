import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()