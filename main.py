import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))