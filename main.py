  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)