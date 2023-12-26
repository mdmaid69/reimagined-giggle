import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)