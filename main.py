import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)