import array
def get_string_from_array(array):
        return array.tobytes()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)