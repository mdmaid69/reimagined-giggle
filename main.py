import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import itertools
print(list(itertools.permutations([1, 2, 3])))