import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()