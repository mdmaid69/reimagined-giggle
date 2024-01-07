import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))