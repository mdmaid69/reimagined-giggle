import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import time
def get_time_since_epoch():
        return time.time()