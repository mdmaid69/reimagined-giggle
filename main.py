import collections
def create_stack():
        return collections.deque()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)