n = 10
print("Square numbers:", [x**2 for x in range(n)])
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)