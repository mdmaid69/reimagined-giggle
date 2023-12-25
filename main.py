import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()