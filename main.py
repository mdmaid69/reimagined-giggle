import math
def calculate_sine(x):
        return math.sin(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread