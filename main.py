import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])