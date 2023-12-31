import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)