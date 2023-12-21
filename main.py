import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}