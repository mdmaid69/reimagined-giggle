import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)