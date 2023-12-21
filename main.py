import time
def get_current_time():
        return time.time()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)