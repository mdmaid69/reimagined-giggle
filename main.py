import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
n = 10
print("Powers of 2:", [2**x for x in range(n)])