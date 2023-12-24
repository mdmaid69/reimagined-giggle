import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread