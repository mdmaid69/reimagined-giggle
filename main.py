import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])