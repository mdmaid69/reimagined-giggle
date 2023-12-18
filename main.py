import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread