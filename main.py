import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
n = 10
print("Square numbers:", [x**2 for x in range(n)])