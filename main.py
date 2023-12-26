import math
def calculate_cosine(x):
        return math.cos(x)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread