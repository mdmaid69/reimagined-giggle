import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)