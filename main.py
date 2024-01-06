import datetime
def get_current_datetime():
        return datetime.datetime.now()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)