text = "Hello, world!"
print("Characters:", len(text))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))