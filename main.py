import random
print(random.randint(0, 100))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))