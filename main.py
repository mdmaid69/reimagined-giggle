import itertools
print(list(itertools.permutations([1, 2, 3])))
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)