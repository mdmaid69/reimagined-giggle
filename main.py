import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread