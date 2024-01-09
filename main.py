print([x**2 for x in range(10)])
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))