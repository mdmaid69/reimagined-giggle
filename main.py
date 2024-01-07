import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)