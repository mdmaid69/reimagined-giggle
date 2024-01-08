import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()