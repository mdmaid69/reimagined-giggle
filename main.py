import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread