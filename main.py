import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def set_array_item(array, i, item):
        array[i] = item