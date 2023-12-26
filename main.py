import math
print(math.pi)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)