import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
n = 10
print("Square numbers:", [x**2 for x in range(n)])