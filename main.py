for i in range(10): print(i)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)