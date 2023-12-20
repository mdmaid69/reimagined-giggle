import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a