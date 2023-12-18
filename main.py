import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)