import math
def calculate_arc_cosine(x):
        return math.acos(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()