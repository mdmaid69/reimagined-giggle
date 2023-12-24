  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])