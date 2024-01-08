import array
def convert_array_to_bytes(array):
        return array.tobytes()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)