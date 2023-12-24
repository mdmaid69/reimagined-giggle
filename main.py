import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)