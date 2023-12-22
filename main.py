import array
def get_array_itemsize(array):
        return array.itemsize
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)