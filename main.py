import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}