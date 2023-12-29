import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import re
def split_string(pattern, string):
        return re.split(pattern, string)