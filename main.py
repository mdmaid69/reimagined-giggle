import array
def get_array_item_count(array, item):
        return array.count(item)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)