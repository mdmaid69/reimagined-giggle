import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)