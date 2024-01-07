import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)