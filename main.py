import time
def get_current_time():
        return time.ctime()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)