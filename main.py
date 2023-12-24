import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))