import datetime
def get_today_date():
        return datetime.date.today()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h