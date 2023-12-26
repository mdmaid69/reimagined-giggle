  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)