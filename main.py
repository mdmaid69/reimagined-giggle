import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))