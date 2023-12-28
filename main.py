import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import collections
def create_queue():
        return collections.deque()