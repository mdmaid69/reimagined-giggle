import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])