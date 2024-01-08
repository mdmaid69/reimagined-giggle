import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)