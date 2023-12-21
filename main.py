import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()