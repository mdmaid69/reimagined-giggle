import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread