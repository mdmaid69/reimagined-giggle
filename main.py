  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import itertools
print(list(itertools.permutations([1, 2, 3])))