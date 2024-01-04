import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def append_to_array(array, item):
        array.append(item)