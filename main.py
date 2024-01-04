import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()