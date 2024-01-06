import time
def get_time_since_epoch():
        return time.time()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h