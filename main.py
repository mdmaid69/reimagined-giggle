import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)