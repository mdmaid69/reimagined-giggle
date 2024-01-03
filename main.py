import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])