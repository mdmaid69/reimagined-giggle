import time
def get_current_time():
        return time.time()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)