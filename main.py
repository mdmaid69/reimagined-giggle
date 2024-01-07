import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import datetime
def get_current_date():
        return datetime.date.today()