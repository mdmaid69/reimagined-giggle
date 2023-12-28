  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])