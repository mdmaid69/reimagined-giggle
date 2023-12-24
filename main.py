import array
def get_array_as_repr(array):
        return repr(array)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)