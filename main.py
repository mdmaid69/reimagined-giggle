import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())