import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)