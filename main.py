import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)