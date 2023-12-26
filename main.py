import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def get_array_itemsize(array):
        return array.itemsize