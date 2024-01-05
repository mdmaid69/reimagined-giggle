n = 10
print("Square numbers:", [x**2 for x in range(n)])
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)