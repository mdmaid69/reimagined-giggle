import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)