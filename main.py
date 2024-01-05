import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)