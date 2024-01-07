import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
n = 10
print("Cube numbers:", [x**3 for x in range(n)])