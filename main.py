import datetime
print(datetime.datetime.now())
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)