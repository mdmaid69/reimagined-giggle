import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import datetime
def get_today_date():
        return datetime.date.today()