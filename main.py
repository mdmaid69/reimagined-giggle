import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import time
def get_current_time():
        return time.ctime()