import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()