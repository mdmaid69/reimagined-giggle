import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b