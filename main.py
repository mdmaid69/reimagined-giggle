import array
def clear_array(array):
        array *= 0
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)