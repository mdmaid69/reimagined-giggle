import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))