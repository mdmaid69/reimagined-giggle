import datetime
def get_current_date():
        return datetime.date.today()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)