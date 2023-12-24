import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))