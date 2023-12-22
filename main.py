import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])