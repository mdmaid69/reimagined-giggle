import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array