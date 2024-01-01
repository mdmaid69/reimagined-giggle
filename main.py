n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)