n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)