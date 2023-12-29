import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)