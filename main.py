import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)