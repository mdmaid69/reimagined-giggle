import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
x = 10
y = 20
print("Sum:", x + y)