import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread