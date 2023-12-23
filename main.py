print([x**2 for x in range(10)])
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)