import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import datetime
print(datetime.datetime.now())