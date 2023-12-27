for i in range(5):
        print(i)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)