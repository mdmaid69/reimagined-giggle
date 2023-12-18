import itertools
print(list(itertools.permutations([1, 2, 3])))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)