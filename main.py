import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))