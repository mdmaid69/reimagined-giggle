import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread