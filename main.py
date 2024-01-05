import array
def convert_array_to_bytes(array):
        return array.tobytes()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h