print([x**2 for x in range(10)])
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))