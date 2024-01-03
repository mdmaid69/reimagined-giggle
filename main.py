import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)