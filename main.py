import array
def get_bytes_from_array(array):
        return array.tobytes()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)