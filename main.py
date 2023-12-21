import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h