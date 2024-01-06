from collections import Counter
print(Counter("hello world"))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))