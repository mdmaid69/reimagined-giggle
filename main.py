import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import math
def calculate_square_root(x):
        return math.sqrt(x)