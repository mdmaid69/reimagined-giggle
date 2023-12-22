n = 10
print("Powers of 2:", [2**x for x in range(n)])
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))