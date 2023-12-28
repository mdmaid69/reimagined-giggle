n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import re
def split_string(pattern, string):
        return re.split(pattern, string)