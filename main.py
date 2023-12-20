import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import collections
def create_priority_queue():
        return collections.deque()