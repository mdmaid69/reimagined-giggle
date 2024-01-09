  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  def is_even(n):
        return n % 2 == 0