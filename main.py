import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}