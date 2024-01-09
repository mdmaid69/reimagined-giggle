import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)