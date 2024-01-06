import itertools
print(list(itertools.permutations([1, 2, 3])))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)