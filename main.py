import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import time
def get_current_time():
        return time.ctime()