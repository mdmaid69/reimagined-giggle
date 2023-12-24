for i in range(10): print(i)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))