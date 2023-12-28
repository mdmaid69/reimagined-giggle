import math
def calculate_sign(x):
        return math.copysign(1, x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread