import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable