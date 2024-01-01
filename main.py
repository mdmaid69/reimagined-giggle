import array
def check_if_array_contains_item(array, item):
        return item in array
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h