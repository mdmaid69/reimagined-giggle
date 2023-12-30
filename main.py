import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)