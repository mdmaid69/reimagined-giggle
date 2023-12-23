import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))