import collections
def create_priority_queue():
        return collections.deque()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)