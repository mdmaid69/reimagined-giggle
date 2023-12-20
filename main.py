import os
print(os.getcwd())
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))