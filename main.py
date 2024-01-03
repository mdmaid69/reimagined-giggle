import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)