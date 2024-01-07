import math
def calculate_square_root(x):
        return math.sqrt(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread