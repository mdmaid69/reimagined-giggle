import datetime
def get_current_datetime():
        return datetime.datetime.now()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)