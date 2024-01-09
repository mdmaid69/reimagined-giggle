import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))