import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)