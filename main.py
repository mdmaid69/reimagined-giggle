import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)