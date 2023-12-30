import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)