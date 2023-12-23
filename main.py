import itertools
print(list(itertools.permutations([1, 2, 3])))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)