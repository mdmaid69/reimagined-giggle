import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)