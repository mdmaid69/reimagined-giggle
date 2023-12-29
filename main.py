import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)