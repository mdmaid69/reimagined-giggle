import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def cube_number(x):
        return x**3