import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)