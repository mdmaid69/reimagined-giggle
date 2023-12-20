import math
def calculate_error_function(x):
        return math.erf(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread