import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)