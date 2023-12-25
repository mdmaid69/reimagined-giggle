import datetime
def get_current_date():
        return datetime.date.today()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)