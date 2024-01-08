n = 10
print("Powers of 2:", [2**x for x in range(n)])
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)