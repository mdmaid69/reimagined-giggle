def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))