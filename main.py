import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)