import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()