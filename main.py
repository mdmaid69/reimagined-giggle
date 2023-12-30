import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))