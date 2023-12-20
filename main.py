import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def get_array_as_int(array):
        return int(array[0])