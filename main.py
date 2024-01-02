import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)