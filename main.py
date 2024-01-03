import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread