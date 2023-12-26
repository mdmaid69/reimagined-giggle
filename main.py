import array
def get_list_from_array(array):
        return array.tolist()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h