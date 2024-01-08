import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)