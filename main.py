import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)