n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)