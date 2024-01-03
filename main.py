n = 10
print("Square numbers:", [x**2 for x in range(n)])
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)