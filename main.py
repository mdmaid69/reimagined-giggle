import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)