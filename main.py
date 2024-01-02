import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()