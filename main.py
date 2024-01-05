n = 10
print("Powers of 2:", [2**x for x in range(n)])
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)