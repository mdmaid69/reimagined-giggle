import array
def append_to_array(array, item):
        array.append(item)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)