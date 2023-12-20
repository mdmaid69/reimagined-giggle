import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()