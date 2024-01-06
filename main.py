import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread