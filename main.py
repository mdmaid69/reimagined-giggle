import array
def get_array_item_count(array, item):
        return array.count(item)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)