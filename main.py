n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)