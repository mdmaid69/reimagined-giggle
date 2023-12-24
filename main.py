import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def get_list_from_array(array):
        return array.tolist()