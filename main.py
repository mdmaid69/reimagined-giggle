n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))