import array
def get_array_as_memoryview(array):
        return memoryview(array)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)