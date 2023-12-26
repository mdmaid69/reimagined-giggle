import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))