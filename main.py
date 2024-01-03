import re
def split_string(pattern, string):
        return re.split(pattern, string)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))