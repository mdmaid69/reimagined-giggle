n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)