text = "Hello, world!"
print("Reversed:", text[::-1])
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))