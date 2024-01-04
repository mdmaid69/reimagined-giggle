import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a