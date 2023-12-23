import itertools
print(list(itertools.permutations([1, 2, 3])))
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)