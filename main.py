import collections
def create_priority_queue():
        return collections.deque()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)