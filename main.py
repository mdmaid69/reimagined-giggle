import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)