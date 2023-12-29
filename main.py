import time
def get_current_time():
        return time.time()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h