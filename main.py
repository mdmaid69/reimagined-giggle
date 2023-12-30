  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)