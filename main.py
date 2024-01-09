  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)