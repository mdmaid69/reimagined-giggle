import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)