def greet(name):
        print(f"Hello, {name}!")
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))