import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)