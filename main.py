import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def convert_array_to_bytes(array):
        return array.tobytes()