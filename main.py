import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)