import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)