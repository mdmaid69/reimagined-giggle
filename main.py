import itertools
print(list(itertools.permutations([1, 2, 3])))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)