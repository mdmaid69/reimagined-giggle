  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)