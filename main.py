import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)