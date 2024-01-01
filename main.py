import time
print(time.time())
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)