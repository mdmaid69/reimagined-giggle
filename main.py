import array
def extend_array(array, iterable):
        array.extend(iterable)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)