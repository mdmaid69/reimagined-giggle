import array
def clear_array(array):
        array *= 0
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)