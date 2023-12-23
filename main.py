import array
def remove_from_array(array, item):
        array.remove(item)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)