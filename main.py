import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)