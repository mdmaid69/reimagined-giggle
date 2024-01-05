print([x**2 for x in range(10)])
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)