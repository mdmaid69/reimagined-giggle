import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)