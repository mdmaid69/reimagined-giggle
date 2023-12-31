import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)