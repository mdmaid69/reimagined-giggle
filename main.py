import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)