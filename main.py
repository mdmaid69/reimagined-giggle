import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)