import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread