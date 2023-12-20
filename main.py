n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))