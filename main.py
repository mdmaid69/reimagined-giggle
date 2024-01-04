import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)