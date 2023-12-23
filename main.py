import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)