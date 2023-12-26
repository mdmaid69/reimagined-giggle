  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import collections
def create_ordered_dict():
        return collections.OrderedDict()