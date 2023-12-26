import math
def calculate_arc_sine(x):
        return math.asin(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread