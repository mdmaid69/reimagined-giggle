import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import time
def get_time_since_epoch():
        return time.time()