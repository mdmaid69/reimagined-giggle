import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()