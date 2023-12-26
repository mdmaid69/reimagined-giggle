import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def get_array_buffer_info(array):
        return array.buffer_info()