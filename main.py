n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)