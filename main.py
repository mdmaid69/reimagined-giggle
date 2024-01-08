import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread