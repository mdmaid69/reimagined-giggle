import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)