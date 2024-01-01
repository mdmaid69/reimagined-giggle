import itertools
print(list(itertools.permutations([1, 2, 3])))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)