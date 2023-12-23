import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)