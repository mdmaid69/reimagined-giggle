import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))