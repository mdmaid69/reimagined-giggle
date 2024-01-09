import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))