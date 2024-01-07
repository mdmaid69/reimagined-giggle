import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import collections
def create_priority_queue():
        return collections.deque()