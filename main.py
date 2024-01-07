i = 0
while i < 5:
        print(i)
        i += 1
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)