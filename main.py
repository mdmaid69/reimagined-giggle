import sys
print(sys.version)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))