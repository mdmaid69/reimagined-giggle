import random
print(random.randint(0, 100))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)