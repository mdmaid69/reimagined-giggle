import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def extend_array(array, iterable):
        array.extend(iterable)