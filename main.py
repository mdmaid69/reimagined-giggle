def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)