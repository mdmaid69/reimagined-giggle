import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)