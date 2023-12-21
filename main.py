import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()