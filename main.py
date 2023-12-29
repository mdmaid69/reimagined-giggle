import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])