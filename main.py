import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a