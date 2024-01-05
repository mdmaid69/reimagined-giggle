n = 10
print("Powers of 2:", [2**x for x in range(n)])
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))