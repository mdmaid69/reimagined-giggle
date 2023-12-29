import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread