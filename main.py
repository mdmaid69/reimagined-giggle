import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h