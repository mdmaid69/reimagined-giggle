import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)