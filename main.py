import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h