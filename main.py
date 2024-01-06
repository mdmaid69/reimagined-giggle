import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
n = 10
print("Powers of 2:", [2**x for x in range(n)])