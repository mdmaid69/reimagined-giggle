import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])