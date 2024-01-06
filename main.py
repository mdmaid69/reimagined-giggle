import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def extend_array(array, iterable):
        array.extend(iterable)