import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()