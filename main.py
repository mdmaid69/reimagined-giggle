import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)