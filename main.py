import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)