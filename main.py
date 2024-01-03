import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3