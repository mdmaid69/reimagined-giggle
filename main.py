import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])