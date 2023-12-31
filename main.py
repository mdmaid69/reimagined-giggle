import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)