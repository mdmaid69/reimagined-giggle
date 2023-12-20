import math
def calculate_exponential(x):
        return math.exp(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread