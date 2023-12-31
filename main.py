import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)