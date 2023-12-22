import math
def calculate_ceiling(x):
        return math.ceil(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread