import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)