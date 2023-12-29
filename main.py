import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
n = 10
print("Cube numbers:", [x**3 for x in range(n)])