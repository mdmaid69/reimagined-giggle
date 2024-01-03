import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def add_numbers(x, y):
        return x + y