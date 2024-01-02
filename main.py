import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def cube_number(x):
        return x**3