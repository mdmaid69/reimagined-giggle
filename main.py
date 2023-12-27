import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread