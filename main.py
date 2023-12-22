import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)