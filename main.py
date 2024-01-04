import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a