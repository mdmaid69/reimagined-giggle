n = 10
print("Powers of 2:", [2**x for x in range(n)])
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)