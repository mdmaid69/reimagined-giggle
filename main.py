import datetime
def get_today_date():
        return datetime.date.today()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)