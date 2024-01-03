import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)