n = 10
print("Square numbers:", [x**2 for x in range(n)])
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)