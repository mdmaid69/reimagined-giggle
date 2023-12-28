import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)