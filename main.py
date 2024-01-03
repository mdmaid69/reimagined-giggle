print(sum(range(10)))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)