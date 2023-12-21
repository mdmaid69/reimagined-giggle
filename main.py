import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()