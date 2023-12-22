import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)