import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def square_number(x):
        return x**2