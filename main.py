import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)