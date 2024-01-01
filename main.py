def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)