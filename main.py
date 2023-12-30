import numpy as np
print(np.array([1, 2, 3]))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))