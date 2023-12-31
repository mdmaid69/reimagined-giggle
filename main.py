import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def get_array_buffer_info(array):
        return array.buffer_info()