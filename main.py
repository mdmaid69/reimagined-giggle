import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread