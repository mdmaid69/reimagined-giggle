import time
def get_time_since_epoch():
        return time.time()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))