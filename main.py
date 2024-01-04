import math
def calculate_absolute_value(x):
        return math.fabs(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()