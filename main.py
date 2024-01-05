import os
print(os.getcwd())
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)