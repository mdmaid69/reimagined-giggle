import array
def get_array_as_complex(array):
        return complex(array[0])
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)