import math
def calculate_absolute_value(x):
        return math.fabs(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread