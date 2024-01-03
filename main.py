  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))