import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)