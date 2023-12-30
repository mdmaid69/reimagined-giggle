import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)