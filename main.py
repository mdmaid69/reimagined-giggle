import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)