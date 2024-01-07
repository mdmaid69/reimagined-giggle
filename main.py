import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread