import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)