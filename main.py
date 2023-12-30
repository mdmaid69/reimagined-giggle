import time
def get_time_since_epoch():
        return time.time()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)