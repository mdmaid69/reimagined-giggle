import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def greet(name):
        print(f"Hello, {name}!")