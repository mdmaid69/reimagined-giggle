import collections
def create_ordered_dict():
        return collections.OrderedDict()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h