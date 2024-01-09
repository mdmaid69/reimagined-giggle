import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])