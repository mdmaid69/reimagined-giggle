import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def iterate_over_array(array):
        for item in array:
        print(item)