n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)