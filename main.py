import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()