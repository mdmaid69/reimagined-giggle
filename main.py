import itertools
print(list(itertools.permutations([1, 2, 3])))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)