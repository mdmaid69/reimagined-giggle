import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)