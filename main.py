import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b