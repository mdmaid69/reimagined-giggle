import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)