import array
def remove_from_array(array, item):
        array.remove(item)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)