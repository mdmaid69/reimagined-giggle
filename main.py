import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))