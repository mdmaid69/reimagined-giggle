print("Hello, world!")
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))