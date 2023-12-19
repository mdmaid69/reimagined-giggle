import array
def iterate_over_array(array):
        for item in array:
        print(item)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h