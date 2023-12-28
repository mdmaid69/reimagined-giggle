import math
def calculate_arc_cosine(x):
        return math.acos(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread