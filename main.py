import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
n = 10
print("Square numbers:", [x**2 for x in range(n)])