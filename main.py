import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])