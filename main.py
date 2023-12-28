import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
n = 10
print("Powers of 2:", [2**x for x in range(n)])