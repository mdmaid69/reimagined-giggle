print(sum(range(10)))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))