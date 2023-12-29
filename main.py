import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread