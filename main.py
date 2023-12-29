import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import time
print(time.time())