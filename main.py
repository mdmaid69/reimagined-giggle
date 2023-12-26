import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import re
def split_string(pattern, string):
        return re.split(pattern, string)