import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import time
def get_current_time():
        return time.ctime()