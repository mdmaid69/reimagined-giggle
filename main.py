import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)