import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h