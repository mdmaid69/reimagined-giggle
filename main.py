import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
n = 10
print("Powers of 2:", [2**x for x in range(n)])