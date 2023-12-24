import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
print([x**2 for x in range(10)])