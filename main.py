import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)