import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)