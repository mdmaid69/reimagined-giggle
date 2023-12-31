import sys
print(sys.version)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))