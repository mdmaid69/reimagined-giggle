import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)