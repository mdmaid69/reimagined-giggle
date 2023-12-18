import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def get_bytes_from_array(array):
        return array.tobytes()