import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))