import math
def calculate_gamma_function(x):
        return math.gamma(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread