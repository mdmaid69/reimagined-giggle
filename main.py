import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])