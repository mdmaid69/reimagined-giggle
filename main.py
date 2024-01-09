import datetime
def get_current_datetime():
        return datetime.datetime.now()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h