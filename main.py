import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
n = 10
print("Powers of 2:", [2**x for x in range(n)])