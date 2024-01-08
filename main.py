import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()