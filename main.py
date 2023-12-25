import array
def set_array_item(array, i, item):
        array[i] = item
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)