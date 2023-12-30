import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)