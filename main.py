n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))