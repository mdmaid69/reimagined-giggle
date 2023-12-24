import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import itertools
print(list(itertools.permutations([1, 2, 3])))