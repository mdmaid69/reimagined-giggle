n = 10
print("Powers of 2:", [2**x for x in range(n)])
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)