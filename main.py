n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)