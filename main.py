import re
def split_string(pattern, string):
        return re.split(pattern, string)
import itertools
print(list(itertools.permutations([1, 2, 3])))