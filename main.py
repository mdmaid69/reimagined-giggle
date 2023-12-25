n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)