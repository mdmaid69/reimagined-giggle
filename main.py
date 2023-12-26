import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days