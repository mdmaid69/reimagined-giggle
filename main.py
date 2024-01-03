import math
def calculate_arc_tangent(x):
        return math.atan(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread