import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def greet(name):
        print(f"Hello, {name}!")