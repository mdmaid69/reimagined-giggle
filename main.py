import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))