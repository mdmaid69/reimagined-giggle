import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import itertools
print(list(itertools.permutations([1, 2, 3])))