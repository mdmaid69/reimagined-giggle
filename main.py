import datetime
def get_current_date():
        return datetime.date.today()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)