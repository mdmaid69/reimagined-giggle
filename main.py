n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)