n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)