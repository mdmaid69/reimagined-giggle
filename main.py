from collections import Counter
print(Counter("hello world"))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)