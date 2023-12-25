import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread