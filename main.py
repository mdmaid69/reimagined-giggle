import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())