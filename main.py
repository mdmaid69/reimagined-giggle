  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))