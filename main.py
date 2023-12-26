import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))