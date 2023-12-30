import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())