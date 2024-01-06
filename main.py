import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)