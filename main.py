import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)