import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
from collections import Counter
print(Counter("hello world"))