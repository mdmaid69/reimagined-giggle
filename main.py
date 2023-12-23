import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)