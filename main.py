import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)