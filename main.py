import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import time
def get_time_since_epoch():
        return time.time()