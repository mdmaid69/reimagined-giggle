n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)