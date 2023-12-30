import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()