for i in range(10): print(i)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)