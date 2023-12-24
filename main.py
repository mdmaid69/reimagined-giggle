import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def greet(name):
        print(f"Hello, {name}!")