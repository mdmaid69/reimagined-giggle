  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))