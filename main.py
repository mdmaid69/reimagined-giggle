import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)