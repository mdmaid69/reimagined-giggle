import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread