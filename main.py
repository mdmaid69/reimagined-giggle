import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)