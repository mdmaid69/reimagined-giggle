import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()