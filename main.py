numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)