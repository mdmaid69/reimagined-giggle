n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)