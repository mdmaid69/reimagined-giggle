import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
for i in range(10): print(i)