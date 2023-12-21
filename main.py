import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))