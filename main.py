import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)