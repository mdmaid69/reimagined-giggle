import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import datetime
def get_today_date():
        return datetime.date.today()