import datetime
print(datetime.datetime.now())
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)