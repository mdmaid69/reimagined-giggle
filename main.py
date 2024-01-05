import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3