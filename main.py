import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))