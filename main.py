import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread