import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))