import array
def reverse_array(array):
        array.reverse()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)