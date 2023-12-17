import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)