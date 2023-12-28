for i in range(5):
        print(i)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)