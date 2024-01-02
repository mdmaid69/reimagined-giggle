import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
from collections import Counter
print(Counter("hello world"))