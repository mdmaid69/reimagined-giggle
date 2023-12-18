import random
print(random.randint(0, 100))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))