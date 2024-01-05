import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)