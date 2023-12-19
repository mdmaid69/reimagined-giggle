  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  def convert_to_octal(n):
        return oct(n)