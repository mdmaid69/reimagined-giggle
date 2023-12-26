import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)