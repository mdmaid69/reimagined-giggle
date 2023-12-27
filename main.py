import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])