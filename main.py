import array
def get_array_slice(array, i, j):
        return array[i:j]
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)