import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h