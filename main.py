import itertools
print(list(itertools.permutations([1, 2, 3])))
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)