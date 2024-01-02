import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
n = 10
print("Square numbers:", [x**2 for x in range(n)])