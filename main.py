import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
x = 10
y = 20
print("Sum:", x + y)