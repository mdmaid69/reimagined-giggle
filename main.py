import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height