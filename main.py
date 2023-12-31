import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)