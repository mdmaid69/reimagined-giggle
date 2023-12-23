import numpy as np
print(np.array([1, 2, 3]))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)