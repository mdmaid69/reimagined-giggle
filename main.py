import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()