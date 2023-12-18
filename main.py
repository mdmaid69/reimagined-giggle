import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array