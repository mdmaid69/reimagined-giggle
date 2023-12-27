import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
n = 10
print("Square numbers:", [x**2 for x in range(n)])