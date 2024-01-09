from collections import Counter
print(Counter("hello world"))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)