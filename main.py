import collections
def create_priority_queue():
        return collections.deque()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)