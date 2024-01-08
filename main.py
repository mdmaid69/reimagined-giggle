import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)