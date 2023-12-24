import array
def get_array_as_int(array):
        return int(array[0])
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)