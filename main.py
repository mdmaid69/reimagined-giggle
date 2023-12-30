import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)