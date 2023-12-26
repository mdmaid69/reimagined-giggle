import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)