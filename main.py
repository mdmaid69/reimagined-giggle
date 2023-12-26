import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
for i in range(5):
        print(i)