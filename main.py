import numpy as np
print(np.array([1, 2, 3]))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)