import sys
print(sys.version)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))