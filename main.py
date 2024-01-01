import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def check_if_array_contains_item(array, item):
        return item in array