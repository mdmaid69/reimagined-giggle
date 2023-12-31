import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h