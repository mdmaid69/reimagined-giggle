import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread