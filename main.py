print([x**2 for x in range(10)])
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))