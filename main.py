for i in range(5):
        print(i)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))