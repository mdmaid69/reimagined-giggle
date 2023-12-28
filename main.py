import math
def calculate_floor(x):
        return math.floor(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread