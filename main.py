i = 0
while i < 5:
        print(i)
        i += 1
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)