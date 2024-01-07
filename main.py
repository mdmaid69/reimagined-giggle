import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
n = 10
print("Square numbers:", [x**2 for x in range(n)])