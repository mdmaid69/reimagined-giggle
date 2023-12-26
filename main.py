print([x**2 for x in range(10)])
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)