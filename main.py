import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a