import math
def calculate_factorial(n):
        return math.factorial(n)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread