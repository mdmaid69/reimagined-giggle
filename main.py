import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def iterate_over_array(array):
        for item in array:
        print(item)