import datetime
def get_today_date():
        return datetime.date.today()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)