import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)