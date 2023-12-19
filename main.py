import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()