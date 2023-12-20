import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def check_if_array_contains_item(array, item):
        return item in array