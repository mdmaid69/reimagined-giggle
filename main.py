import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())