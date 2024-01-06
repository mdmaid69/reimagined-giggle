import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)