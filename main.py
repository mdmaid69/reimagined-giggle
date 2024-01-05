import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)