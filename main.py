  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)