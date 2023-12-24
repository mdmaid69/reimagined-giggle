import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height