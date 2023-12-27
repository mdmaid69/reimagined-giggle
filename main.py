import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)