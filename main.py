import array
def get_array_item_count(array, item):
        return array.count(item)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h