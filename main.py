import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
from collections import Counter
print(Counter("hello world"))