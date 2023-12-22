import collections
def create_ordered_dict():
        return collections.OrderedDict()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)