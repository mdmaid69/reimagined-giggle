import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h