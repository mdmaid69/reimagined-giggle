print(sum(range(10)))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)