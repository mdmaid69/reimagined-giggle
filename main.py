import re
def split_string(pattern, string):
        return re.split(pattern, string)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))