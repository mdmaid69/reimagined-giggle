import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread