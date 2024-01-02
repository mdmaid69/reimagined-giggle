n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))