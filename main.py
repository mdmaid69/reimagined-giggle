import array
def convert_array_to_list(array):
        return array.tolist()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h