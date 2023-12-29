import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))