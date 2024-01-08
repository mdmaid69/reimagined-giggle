import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()