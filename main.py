import time
def get_current_time():
        return time.ctime()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h