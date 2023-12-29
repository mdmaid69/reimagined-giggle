import time
print(time.time())
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)