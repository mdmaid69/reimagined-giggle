import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread