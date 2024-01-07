import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import re
def split_string(pattern, string):
        return re.split(pattern, string)