import datetime
def get_current_date():
        return datetime.date.today()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)