import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())