import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def is_odd(n):
        return n % 2 != 0