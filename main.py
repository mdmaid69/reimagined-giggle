import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b