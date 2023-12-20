n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))