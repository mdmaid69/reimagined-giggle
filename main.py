import sys
print(sys.version)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)