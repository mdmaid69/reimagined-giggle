import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))