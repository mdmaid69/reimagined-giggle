import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)