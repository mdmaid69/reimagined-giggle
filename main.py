import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)