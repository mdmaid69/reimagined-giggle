import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a