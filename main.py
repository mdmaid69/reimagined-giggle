import array
def convert_array_to_list(array):
        return array.tolist()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)