n = 10
print("Powers of 2:", [2**x for x in range(n)])
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)