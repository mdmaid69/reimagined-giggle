from collections import Counter
print(Counter("hello world"))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))