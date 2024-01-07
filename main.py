n = 10
print("Powers of 2:", [2**x for x in range(n)])
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)