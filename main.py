import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_circle_area(radius):
        return math.pi * radius**2