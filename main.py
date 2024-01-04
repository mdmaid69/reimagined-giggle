n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)