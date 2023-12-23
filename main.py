import sys
print(sys.version)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)