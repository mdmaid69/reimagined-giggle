import array
def convert_array_to_unicode(array):
        return array.tounicode()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h