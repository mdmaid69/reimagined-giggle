import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import time
def get_current_time():
        return time.time()